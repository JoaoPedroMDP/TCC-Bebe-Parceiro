import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InspectEvaluationComponent } from './inspect-evaluation.component';

describe('InspectEvaluationComponent', () => {
  let component: InspectEvaluationComponent;
  let fixture: ComponentFixture<InspectEvaluationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InspectEvaluationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InspectEvaluationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
