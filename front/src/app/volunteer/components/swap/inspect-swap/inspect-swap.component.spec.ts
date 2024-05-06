import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InspectSwapComponent } from './inspect-swap.component';

describe('InspectSwapComponent', () => {
  let component: InspectSwapComponent;
  let fixture: ComponentFixture<InspectSwapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InspectSwapComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InspectSwapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
